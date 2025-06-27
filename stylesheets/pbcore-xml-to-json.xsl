<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <xsl:output method="text" encoding="UTF-8" />
  <xsl:strip-space elements="*" />

  <!-- Hardcoded list of repeatable elements -->
  <xsl:variable name="repeatable"
    select="' pbcoreAssetType pbcoreAssetDate pbcoreIdentifier pbcoreTitle pbcoreSubject pbcoreDescription pbcoreGenre pbcoreRelation pbcoreCoverage pbcoreAudienceLevel pbcoreAudienceRating pbcoreCreator creatorRole pbcoreContributor contributorRole pbcorePublisher publisherRole pbcoreInstantiation pbcoreAnnotation pbcorePart pbcoreExtension instantiationIdentifier instantiationDate instantiationDimensions instantiationGenerations instantiationEssenceTrack instantiationRelation instantiationAnnotation instantiationExtension essenceTrackIdentifier essenceTrackLanguage essenceTrackAnnotation essenceTrackExtension extensionWrap extensionEmbedded '" />

  <!-- Hardcoded list of repeatable elements that have sub-elements -->
  <xsl:variable name="with-sub-elements"
    select="' pbcoreDescriptionDocument pbcoreRelation pbcoreCoverage pbcoreCreator pbcoreContributor pbcorePublisher pbcoreRightsSummary pbcoreExtension pbcoreInstantiation instantiationEssenceTrack instantiationRelation instantiationRights instantiationExtension '" />

  <xsl:template match="/">
    <xsl:text>{"pbcoreDescriptionDocument":</xsl:text>
    <xsl:apply-templates select="*" />
    <xsl:text>}</xsl:text>
  </xsl:template>

  <xsl:template match="*">
    <xsl:text>{</xsl:text>

    <!-- Attributes -->
    <xsl:for-each select="@*">
      <xsl:if test="position() &gt; 1">
        <xsl:text>,</xsl:text>
      </xsl:if>
      <xsl:text>"</xsl:text><xsl:value-of select="name()" /><xsl:text>":"</xsl:text>
      <xsl:call-template
        name="escape-json-string">
        <xsl:with-param name="text" select="." />
      </xsl:call-template>
      <xsl:text>"</xsl:text>
    </xsl:for-each>

    <!-- Text-only node -->
    <xsl:variable
      name="has-attributes" select="count(@*) &gt; 0" />
    <xsl:variable name="name" select="name()" />
    <xsl:variable
      name="has-sub-elements" select="contains($with-sub-elements, concat(' ', $name, ' '))" />

    <xsl:if
      test="not($has-sub-elements)">
      <xsl:if test="$has-attributes">
        <xsl:text>,</xsl:text>
      </xsl:if>
      <xsl:text>"text":"</xsl:text>
      <xsl:call-template
        name="escape-json-string">
        <xsl:with-param name="text" select="normalize-space(.)" />
      </xsl:call-template>
      <xsl:text>"</xsl:text>
    </xsl:if>

    <!-- Children -->
    <xsl:for-each
      select="*">
      <xsl:variable name="child-name" select="name()" />
      <xsl:variable name="is-repeatable"
        select="contains($repeatable, concat(' ', $child-name, ' '))" />
      <xsl:variable
        name="is-first" select="not(preceding-sibling::*[name() = $child-name])" />

      <!-- Only emit once per group -->
      <xsl:if
        test="$is-first">
        <!-- Emit comma if there were attributes, text content, or any prior child group -->
        <xsl:if
          test="position() &gt; 1 or $has-attributes or not($has-sub-elements)">
          <xsl:text>,</xsl:text>
        </xsl:if>

        <xsl:text>"</xsl:text><xsl:value-of
          select="$child-name" /><xsl:text>":</xsl:text>

        <xsl:choose>
          <xsl:when test="$is-repeatable">
            <xsl:text>[</xsl:text>
            <xsl:for-each select="../*[name() = $child-name]">
              <xsl:if test="position() &gt; 1">
                <xsl:text>,</xsl:text>
              </xsl:if>
              <xsl:apply-templates select="." />
            </xsl:for-each>
            <xsl:text>]</xsl:text>
          </xsl:when>
          <xsl:otherwise>
            <xsl:apply-templates select="." />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:if>
    </xsl:for-each>

    <xsl:text>}</xsl:text>
  </xsl:template>

  <!-- Escape double quotes -->
  <xsl:template name="escape-json-string">
    <xsl:param name="text" />
    <xsl:choose>
      <xsl:when test="contains($text, '&quot;')">
        <xsl:value-of select="substring-before($text, '&quot;')" />
        <xsl:text>\&quot;</xsl:text>
        <xsl:call-template
          name="escape-json-string">
          <xsl:with-param name="text" select="substring-after($text, '&quot;')" />
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$text" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>