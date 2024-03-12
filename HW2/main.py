from flask import Flask, Response
from webargs import fields, validate
from webargs.flaskparser import use_kwargs
import database_handler as db


app = Flask(__name__)


@app.route('/')
def index():
    links = [
        '<a href="/order_price">Order price</a>',
        '<a href="/get_all_info_about_track">Track info</a>',
        '<a href="/get_albums_all_tracks_time">Albums time</a>',
        '<a href="/stats_by_city">Stats by city</a>',
    ]

    return '<br>'.join(links)


@app.route('/order_price')
@use_kwargs(
    {
        'country': fields.Str(missing=''),

    },
    location='query'
)
def order_price(country: str):
    query = '''
    SELECT 
    invoices.BillingCountry as country, 
    ROUND(SUM(invoice_items.UnitPrice * invoice_items.Quantity), 2) as sales 
    FROM invoice_items 
    LEFT JOIN invoices ON invoices.invoiceId = invoice_items.invoiceId
    WHERE invoices.BillingCountry {}
    GROUP BY invoices.BillingCountry;
    '''.format(f'= "{country}"' if len(country) else 'IS NOT NULL')

    result = db.execute_query(query)
    return db.format_query_records(result)


@app.route('/get_all_info_about_track')
@use_kwargs(
    {
        'track_id': fields.Int(missing=0, validate=validate.Range(
            min=1, min_inclusive=True
        )),
    },
    location='query'
)
def get_all_info_about_track(track_id: int):
    if not track_id:
        return 'Please specify track_id as GET parameter.'

    query = '''
       SELECT 
       tracks.*, genres.*, media_types.*, albums.*, artists.*, SUM(invoice_items.UnitPrice) as sales
       FROM invoice_items
       LEFT JOIN tracks ON tracks.trackId = invoice_items.TrackId
       LEFT JOIN genres ON genres.GenreId = tracks.GenreId
       LEFT JOIN media_types ON media_types.mediaTypeId = tracks.mediaTypeId
       LEFT JOIN albums ON albums.AlbumId = tracks.AlbumId
       LEFT JOIN artists ON artists.ArtistId = albums.ArtistId
       WHERE tracks.TrackId =  {}
       GROUP BY invoice_items.trackId
       '''.format(track_id)

    result = db.execute_query(query)
    return db.format_query_records(result)


@app.route('/get_albums_all_tracks_time')
def get_albums_all_tracks_time():
    query = '''
       SELECT 
       albums.*, ROUND(SUM(milliseconds * 1.0) / 3600000, 2) as album_time
       FROM tracks
       LEFT JOIN albums ON albums.AlbumId = tracks.AlbumId
       GROUP BY albums.AlbumId
       '''

    result = db.execute_query(query)
    return db.format_query_records(result)


@app.route('/stats_by_city')
@use_kwargs(
    {
        'genre': fields.Str(missing=None),
    },
    location='query'
)
def stats_by_city(genre: str):
    params = {}
    if not genre:
        return 'Please specify genre as GET parameter.'
    params['genre'] = genre

    query = '''
          SELECT 
          invoices.BillingCity, COUNT(invoice_items.InvoiceLineId) as counter
          FROM invoice_items
          LEFT JOIN invoices ON invoices.InvoiceId = invoice_items.InvoiceId
          LEFT JOIN tracks ON tracks.TrackId = invoice_items.TrackId
          LEFT JOIN genres ON genres.GenreId = tracks.GenreId
          WHERE genres.Name = ?
          GROUP BY invoices.BillingCity
          ORDER BY counter DESC
          LIMIT 1
          '''

    result = db.execute_query(query=query, args=tuple(params.values()))
    return db.format_query_records(result)
