SELECT
	countrylanguage.Language,
    ROUND(SUM(countrylanguage.Percentage * country.Population/100), 2) as TotalSpeaker
FROM
	world.countrylanguage
    INNER JOIN
    world.country
    ON
    countrylanguage.CountryCode = country.Code
GROUP BY
	countrylanguage.Language
ORDER BY
	TotalSpeaker Desc
Limit 1