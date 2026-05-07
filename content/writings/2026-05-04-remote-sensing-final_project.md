---
title: Agricultural drought dynamics in Uttar Pradesh
date: 2026-04-20
description: Uttar Pradesh is vulnerable to drought and in recent years it 
draft: false
math: true
---

> Note: This was a class project for my course *Geospatial Technology 2: Remote Sensing of the Environment*. It was done in a very short timeframe and does not guarantee the accuracy of results. 

![Agricultural Drought](/images/drought.jpg)
*Image: Ujjwal Nagar*

## Why I chose this project

I was born and brought up in a small agricultural family in Uttar Pradesh. I did all my schooling there, moved to a few places, and finally landed up here in Bengaluru. Even if I stay here, my heart is still back home. All my life I have seen farming and I was personally engaged in many activities of my family. I am old enough to remember how my family had difficult times irrigating fields and sometimes our crops, like bajra, were entirely dependent on rainfall. Then came the submersible borewell and most of the problems were gone. I remember the day we had our first submersible and the first time it pumped water. That was such a euphoric moment for my family. 

Today I am here at Azim Premji University, Bengaluru --- studying Environmental Science and Sustainability. Realizing how vulnerable our farmers actually are breaks my heart. Those submersible pumps were never the solution, maybe just a temporary band-aid for a deeper wound. This is quite evident from the depleting water levels making those same submersible pumps fail. 

I have long known that Uttar Pradesh is drought-prone and that this is not a new phenomenon for our state. However, I didn't know much about the impact of agriculture. So, when I was asked to do a project for my remote sensing course, this was one of the things that struck my mind. Why not do a project assessing how drought is affecting agriculture in the state of Uttar Pradesh? This is how this whole project was born.

---

# Background

Drought is a hydro-meteorological phenomenon generally caused by the lack of rainfall, which leads to loss of soil moisture. It can cause devastating effects on humans as well as all living beings and ecosystems. While uncommon around some parts of the world, this phenomenon mostly affects the tropics and nearby regions. In India, there is an occurrence of drought almost every two years, hence it is not uncommon for India. The intensity of drought can be exacerbated by phenomena like El Niño and other meteorological events. Hence, it is imperative that we monitor, assess, and analyse the spatio-temporal patterns of drought in our country to reduce the harm caused by it.

## How to define drought?

It may sound surprising, but different countries define drought differently. In simple language, it is regarded as a lack of rainfall, but this simple definition is also the controversial one. The threshold of 'how much less is less' is the controversial part. This threshold can differ depending on how much a lack of rainfall causes trouble, and obviously, it depends on which sector you are talking about. For example, in a country like India, our crops are tuned to rainfall with many regions being entirely dependent on it. But this dependency varies depending on the crops as well as the water requirements of each crop. This makes it difficult to come to an agreement on how much lack of rainfall can be declared as a drought.

Different countries define drought by observing the rainfall patterns of their respective regions. In India, The India Meteorological Department (IMD) defines drought as:

*"In any area when the rainfall deficiency in that area is ≥26% of its long term normal.*" 

When decalring a drought for the country as a whole, it is defined as:
*"When the rainfall deficiency exceeds 10% and when the area under drought exceeds 20% of the total area of the plains in the country, such a situation is considered as drought for the country as a whole."*

## Agricultural drought and its impacts

In India, agriculture provides livelihood support to about 42.3 per cent of the population, which is just a little less than half the population of this country. This is an astounding figure given the size of our population. That is why any adverse impact on agriculture will have a detrimental effect on the lives of so many people. Drought is one of those things that have impacted and can impact agriculture in a severe way. It can lead to food shortages and can have a devastating effect on the economy. So, in this project I will be assessing how agricultural drought has varied over the last 15 years.

I will be using the VHI (Vegetation Health Index) to see how the cropland area has been affected by drought over the years. VHI has shown very good results when analysing the health of vegetation. Before you compute VHI, you need to compute the Temperature Condition Index (TCI) and Vegetation Condition Index (VCI), both of which are precursors for calculating VHI.

**Vegetation Condition Index (VCI)**

$$
VCI = \frac{NDVI - NDVI_{min}}{NDVI_{max} - NDVI_{min}} \times 100
$$

Where:
- $NDVI$ = Normalized Difference Vegetation Index for the current period
- $NDVI_{min}$ = Long-term minimum NDVI for the same period
- $NDVI_{max}$ = Long-term maximum NDVI for the same period

**Temperature Condition Index (TCI)**

$$
TCI = \frac{LST_{max} - LST}{LST_{max} - LST_{min}} \times 100
$$

Where:
- $LST$ = Land Surface Temperature for the current period
- $LST_{min}$ = Long-term minimum LST for the same period
- $LST_{max}$ = Long-term maximum LST for the same period

**Vegetation Health Index (VHI)**

$$
VHI = \alpha \times VCI + (1 - \alpha) \times TCI
$$

Where:
- $VCI$ = Vegetation Condition Index
- $TCI$ = Temperature Condition Index
- $\alpha$ = Weighting coefficient (typically $\alpha = 0.5$, assuming equal contribution)


# Objective

Evaluation of  agricultural drought and vegetation health conditions in Uttar Pradesh using MODIS-based Vegetation Health Index (VHI) from 2010 to 2025.

- To derive NDVI and LST from MODIS satellite data for the study period.
- To compute VCI, Temperature Condition Index (TCI), and Vegetation Health Index (VHI) for the identification of drought-affected areas.
- To analyze annual variability and spatial patterns in vegetation health across the state using VHI classification.

## Data

| Parameter | Landsat | MODIS |
|---|---|---|
| Sensor | OLI (Optical) | Terra/Aqua |
| Product Used | LC08-Collection-2 Level-2 | MOD13Q1, MOD11A2 |
| Spatial Resolution | 30 m (optical) | 250 m (NDVI), 1 km (LST) |
| Temporal Resolution | 16 days | 8 days (LST), 16 days (NDVI) |
| Bands Used | Band 2-7 | NDVI band, LST Day 1km |
| Application | LULC Classification | VCI, TCI, VHI Computation |

Apart from these Global Administrative Unit Layers (GAUL) from FAO was used to get administrative boundaries for the study area. 


## Methodology

Most of the data was processed on the Google Earth Engine platform. 


1. Following preprocessing steps were applied on the datasets (Cloud Masking, Scaling).
2. NDVI Composite for each month was generated from the MODIS NDVI dataset.
3. Minimum NDVI for each month was calculated from the above dataset.
4. VCI was calculated for each image in the monthly image collection.
5. Monthly VCI was aggregated to Yearly VCI.
6. QA mask was applied to select only high-quality pixels.
8. Minimum and Maximum LST were calculated.
9. TCI was calculated for each image.
10. Using the generated TCI, VHI was calculated.
11. Landsat 8 data was downloaded, preprocessed, scaled, and mosaicked into a single raster.
12. Training samples were generated using the TerrSet software.
13. The data was classified into different LULC Classes.
14. A cropland mask was created and subtracted from each image.
15. Spatiotemporal maps and the area under each drought category were generated.

![VHI2](/images/rsproject_flow.png)


## Results

The following spatio-temporal maps show the severity of agricultural drought from the year 2010 to 2025. The year 2010 seems to show the highest extent of agriculture drought. The years 2012, 2015, and 2018 also show major extents of drought across the state. However, most of the area seems to be under the mild category of drought.

![VHI1](/images/vhi_landscape_1.png)

From 2018 to 2025, there doesn't seem to be much impact on vegetation, only the year 2018 seems to have the highest coverage, which is mostly in the mild category. Some parts of Eastern and Central UP seem to always have some occurrence of drought.

![VHI2](/images/vhi_landscape_2.png)

When it comes to the area under different drought categories, 2010 shows the highest extent, especially in the mild category. In the last 5 years, the area under drought appears to remain more or less the same. The years 2010 and 2016 seem to have affected a large portion of the area.

![VHI1](/images/vhi_area.png)

These results also have some limitation when it comes to fully assessing agricultural drought. VHI is an indicator of vegetation health condition not of drought, it is possible there may be other factors affecting the vegetation. Secondly, I use an yearly average to aggregated the results which may not be the best method and can affect results.


## Acknowledgement

I would like to express my sincere gratitude to **Professor Neeti**, *School of Climate Change and Sustainability*, for her continuous support. I would also like to thank **Jahana Shirin K, Muhammed Thwahir and Noor** for their continuous help throughout the duration of this project.
Their expertise and encouragement were instrumental in shaping this project.

## References

- Shewale, M. P., & Kumar, S. (2005). *Climatological features of drought incidences in India* (Meteorological Monograph Climatology No. 21/2005). National Climate Centre, India Meteorological Department. <https://imdpune.gov.in/Reports/drought.pdf>
- Ministry of Finance, Government of India. (2024, July 22). *Agriculture sector has registered an average annual growth rate of 4.18 per cent over the last five years: Economic survey* (Press release). Press Information Bureau. <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2034943&reg=3&lang=2>
- Copernicus Emergency Management Service. (2025, August 11). *Global drought observatory report* (Interactive map report). European Commission. <https://drought.emergency.copernicus.eu/tumbo/gdo/report/?lon=84.016&lat=27.0378&date=2025-08-11>
- Singh, V. (2025, January 29). *Water-guzzling crops push Uttar Pradesh to the brink of a groundwater crisis.* Down to Earth. <https://www.downtoearth.org.in/water/water-guzzling-crops-push-uttar-pradesh-to-the-brink-of-a-groundwater-crisis>
- Food and Agriculture Organization of the United Nations. (2015). *FAO GAUL: Global administrative unit layers 2015, level 0* (Dataset). Google Earth Engine. <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level0>
- Didan, K. (2021). *MOD13Q1.061 Terra vegetation indices 16-day global 250m* (Dataset). NASA LP DAAC via Google Earth Engine. <https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD13Q1>
- Wan, Z., Hook, S., & Hulley, G. (2021). *MOD11A2.061 Terra land surface temperature and emissivity 8-day global 1km* (Dataset). NASA LP DAAC via Google Earth Engine. <https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A2>
- U.S. Geological Survey. (2013). *Landsat 8 collection 2 tier 1 level 2* (Dataset). Google Earth Engine. <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2>

