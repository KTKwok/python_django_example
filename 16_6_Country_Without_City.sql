SELECT
	Country.Name
FROM
	world.country
    LEFT JOIN
    world.city
    ON
    country.Code = city.CountryCode
WHERE
	city.ID IS NULL
ORDER BY
	country.Name