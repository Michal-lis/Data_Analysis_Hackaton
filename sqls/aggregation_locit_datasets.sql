-- dodaj Where = kraków, dodaj groupby count i policz rózne sklepy itp

SELECT
ld1.eurogrid_0250,
ld1.geometria92,
ld2.populacja_razem,
ld2.budynki_all,
ld2.budynki_mieszkalne,
ld3.dochod_bud_pra,
ld4.nazwa_pow,
ld4.nazwa_gmi,
poi.geometria92
FROM locit_datasets.grid250 ld1
LEFT JOIN locit_datasets.grid250_demo_ext ld2
ON ld1.eurogrid_0250=ld2.eurogrid_0250
LEFT JOIN locit_datasets.grid250_dochod ld3
ON ld1.eurogrid_0250=ld3.eurogrid_0250
LEFT JOIN locit_datasets.grid250_miejsc ld4
ON ld1.eurogrid_0250=ld4.eurogrid_0250
LEFT JOIN locit_datasets.poi poi
ON ld1.geometria92=poi.geometria92
LIMIT 50;

/* count bus stops in 1500m from point */
SELECT COUNT(*) AS liczba_przystanków
FROM locit_datasets.poi
WHERE poi_guid IN (
  SELECT ldp.poi_guid
  FROM locit_datasets.poi ldp
  WHERE ldp.poi_subcategory_name='Przystanek autobusowy'
) AND ST_Distance_sphere(ST_SetSRID(ST_MakePoint(20, 50),4674), ST_Centroid(ST_TRANSFORM(geometria92,4674) )) < 1500

