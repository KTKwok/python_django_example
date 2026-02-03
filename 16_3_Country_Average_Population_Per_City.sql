SELECT
	country.Code,
    COUNT(city.ID) as num_of_city,
    ROUND(country.Population/COUNT(city.ID),2) as avg_pop_per_city
FROM
	world.country
    LEFT JOIN
    world.city
    ON
    country.Code = city.CountryCode
WHERE
	city.ID IS NOT NULL
GROUP BY
	country.Code