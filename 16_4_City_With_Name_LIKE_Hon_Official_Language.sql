SELECT
	city.Name,
    country.Name
FROM
	world.city
    INNER JOIN
    world.country
    ON
    city.CountryCode = country.code
    INNER JOIN
    world.countrylanguage
    ON
    country.code = countrylanguage.CountryCode
WHERE
	countrylanguage.IsOfficial = "T"
    AND
    city.Name LIKE "Hon%"