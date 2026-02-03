SELECT
	country.Continent,
    countrylanguage.Language,
    SUM((country.Population * countrylanguage.Percentage)/100) as lang_pop,
    sum_pop_by_continent.sum_pop, 
    (SUM((country.Population * countrylanguage.Percentage)/100)/sum_pop_by_continent.sum_pop)*100 as percent
FROM
	world.country
    INNER JOIN
    world.countrylanguage
    ON
    country.Code = countrylanguage.CountryCode
    INNER JOIN
    (SELECT SUM(Population) as sum_pop, country.Continent FROM world.country GROUP BY country.Continent) as sum_pop_by_continent
    ON
    sum_pop_by_continent.Continent = country.Continent
GROUP BY
	country.Continent, countrylanguage.Language
ORDER BY
	country.Continent, countrylanguage.Language