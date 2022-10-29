--SELECT * FROM albums a
--JOIN artists a2
--ON a.ArtistID = a2.ArtistId;

CREATE VIEW IF NOT EXISTS v_rock_songs
AS 
SELECT t.Name TrackName, 
	a.Title  AlbumTitle,
	a2.Name ArtistName,
	g.Name Genre,
	mt.Name MediaType,
	t.Milliseconds time_ms,
	t.Milliseconds/1000 seconds,
	t.Milliseconds/(1000*60) minutes,
	t.UnitPrice 
FROM tracks t
JOIN albums a 
ON t.AlbumId = a.AlbumId 
JOIN artists a2 
ON a.ArtistId = a2.ArtistId 
JOIN genres g 
ON t.GenreId = g.GenreId 
JOIN media_types mt 
ON t.MediaTypeId = mt.MediaTypeId
WHERE Genre = "Rock"
ORDER BY seconds DESC

SELECT * FROM v_rock_songs vrs ;