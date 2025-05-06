<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <xsl:output method="text" encoding="UTF-8"/>
  <xsl:strip-space elements="*"/>

  <!-- Hardcoded list of multi-occurrence elements -->
  <xsl:variable name="repeatable" select="'pbcoreIdentifier pbcoreTitle pbcoreSubject pbcoreDescription pbcoreGenre pbcoreRelation pbcoreCoverage pbcoreAudienceLevel pbcoreAudienceRating pbcoreCreator pbcoreContributor pbcorePublisher pbcoreRightsSummary instantiation extension annotation'"/>

  <xsl:key name="by-name" match="*" use="name()" />

  <xsl:template match="/">
    <xsl:text>{&#10;  "pbcoreDescriptionDocument": </xsl:text>
    <xsl:apply-templates select="*"/>
    <xsl:text>&#10;}</xsl:text>
  </xsl:template>

  <xsl:template match="*">
    <xsl:param name="indent" select="'  '"/>
    <xsl:text>{</xsl:text>

    <xsl:variable name="has-attributes" select="count(@*) &gt; 0"/>
    <xsl:variable name="has-text" select="normalize-space(.) != '' and count(*) = 0"/>
    <xsl:variable name="has-children" select="count(*) &gt; 0"/>
    <xsl:variable name="children" select="*"/>

    <!-- Attributes -->
    <xsl:for-each select="@*">
      <xsl:if test="position() &gt; 1">
        <xsl:text>,</xsl:text>
      </xsl:if>
      <xsl:text>&#10;</xsl:text>
      <xsl:value-of select="$indent"/>
      <xsl:text>"</xsl:text><xsl:value-of select="name()"/><xsl:text>": "</xsl:text>
      <xsl:call-template name="escape-json-string">
        <xsl:with-param name="text" select="."/>
      </xsl:call-template>
      <xsl:text>"</xsl:text>
    </xsl:for-each>

    <!-- Text content -->
    <xsl:if test="$has-text">
      <xsl:if test="$has-attributes">
        <xsl:text>,</xsl:text>
      </xsl:if>
      <xsl:text>&#10;</xsl:text>
      <xsl:value-of select="$indent"/>
      <xsl:text>"text": "</xsl:text>
      <xsl:call-template name="escape-json-string">
        <xsl:with-param name="text" select="normalize-space(.)"/>
      </xsl:call-template>
      <xsl:text>"</xsl:text>
    </xsl:if>

    <!-- Children grouped by name -->
    <xsl:for-each select="*[generate-id() = generate-id(key('by-name', name())[1])]">
      <xsl:variable name="name" select="name()"/>
      <xsl:if test="$has-attributes or $has-text or position() &gt; 1">
        <xsl:text>,</xsl:text>
      </xsl:if>
      <xsl:text>&#10;</xsl:text>
      <xsl:value-of select="$indent"/>
      <xsl:text>"</xsl:text><xsl:value-of select="$name"/><xsl:text>": </xsl:text>

      <xsl:variable name="is-multi" select="contains(concat(' ', $repeatable, ' '), concat(' ', $name, ' '))"/>
      <xsl:variable name="group" select="key('by-name', $name)"/>

      <xsl:choose>
        <xsl:when test="$is-multi">
          <xsl:text>[</xsl:text>
          <xsl:for-each select="$group">
            <xsl:if test="position() &gt; 1">
              <xsl:text>,</xsl:text>
            </xsl:if>
            <xsl:text>&#10;</xsl:text>
            <xsl:value-of select="concat($indent, '  ')"/>
            <xsl:apply-templates select=".">
              <xsl:with-param name="indent" select="concat($indent, '  ')"/>
            </xsl:apply-templates>
          </xsl:for-each>
          <xsl:text>&#10;</xsl:text>
          <xsl:value-of select="$indent"/>
          <xsl:text>]</xsl:text>
        </xsl:when>
        <xsl:otherwise>
          <xsl:apply-templates select="$group[1]">
            <xsl:with-param name="indent" select="concat($indent, '  ')"/>
          </xsl:apply-templates>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:for-each>

    <xsl:text>&#10;</xsl:text>
    <xsl:value-of select="substring($indent, 1, string-length($indent) - 2)"/>
    <xsl:text>}</xsl:text>
  </xsl:template>

  <!-- Escape double quotes -->
  <xsl:template name="escape-json-string">
    <xsl:param name="text"/>
    <xsl:choose>
      <xsl:when test="contains($text, '&quot;')">
        <xsl:value-of select="substring-before($text, '&quot;')"/>
        <xsl:text>\&quot;</xsl:text>
        <xsl:call-template name="escape-json-string">
          <xsl:with-param name="text" select="substring-after($text, '&quot;')"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$text"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
