from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')
SHOWS_PER_PAGE = 15
SHOWN_PAGE_NUMBERS = 5 # should be odd to have a symmetry in pagination


# @app.route('/shows/')
# @app.route('/shows/<int:page_number>')
# @app.route('/shows/most-rated/')
# @app.route('/shows/most-rated/<int:page_number>')
# @app.route('/shows/order-by-<order_by>/')
# @app.route('/shows/order-by-<order_by>-<order>/')
# @app.route('/shows/order-by-<order_by>/<int:page_number>')
# @app.route('/shows/order-by-<order_by>-<order>/<int:page_number>')
# def shows(page_number=1, order_by="rating", order="DESC"):
#     count = queries.get_show_count()
#     pages_count = math.ceil(count[0]['count'] / SHOWS_PER_PAGE)
#     shows = queries.get_shows_limited(order_by, order, SHOWS_PER_PAGE, (page_number - 1) * SHOWS_PER_PAGE)

#     shown_pages_start = int(page_number - ((SHOWN_PAGE_NUMBERS - 1) / 2))
#     shown_pages_end = int(page_number + ((SHOWN_PAGE_NUMBERS - 1) / 2))
#     if shown_pages_start < 1:
#         shown_pages_start = 1
#         shown_pages_end = SHOWN_PAGE_NUMBERS
#     elif shown_pages_end > pages_count:
#         shown_pages_start = pages_count - SHOWN_PAGE_NUMBERS + 1
#         shown_pages_end = pages_count

#     return render_template(
#         'shows.html',
#         shows=shows,
#         pages_count=pages_count,
#         page_number=page_number,
#         shown_pages_start=shown_pages_start,
#         shown_pages_end=shown_pages_end,
#         order_by=order_by,
#         order=order
#     )


# @app.route('/show/<int:id>/')
# def show(id):
#     show = queries.get_show(id)
#     characters = queries.get_show_characters(id, 3)
#     seasons = queries.get_show_seasons(id)

#     # format character names
#     show['characters_str'] = \
#         ', '.join([character['name'] for character in characters])

#     # getting trailer id from URL to embed video
#     show['trailer_id'] = \
#         show['trailer'][show['trailer'].find('=')+1:] if show['trailer'] else ''

#     # format runtime
#     hours, minutes = divmod(show['runtime'], 60)
#     runtime_str = (str(hours)+'h ' if hours else '') + (str(minutes)+'min' if minutes else '')
#     show['runtime_str'] = runtime_str

#     return render_template('show.html', show=show, seasons=seasons)


# def main():
#     app.run(debug=False)


# if __name__ == '__main__':
#     main()



@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/api/get-most-rated-shows')
def most_rated_shows():
    return jsonify(queries.get_fifteen_most_rated_shows())


@app.route('/api/get-actors-detail')
def get_actors_detail():
    return jsonify(queries.get_actor_detail())


@app.route('/api/get-genres')
def get_genres():
    return jsonify(queries.get_genres_by_limit())


@app.route('/api/get-ordered-shows/<order>')
def get_shows_by_order(order):
    return jsonify(queries.get_shows_by_episode_count(order))


@app.route('/api/get-genres-detail/<int:genre_id>')
def get_genre_details(genre_id):
    return jsonify(queries.get_genre_by_limit(genre_id))


@app.route('/actors')
@app.route('/actors/<name>')
def display_hundred_actor():
    return render_template('list-actors.html')


@app.route('/shows/genres')
def genre():
    return render_template('genres.html')


@app.route('/shows/most-rated')
def shows():
    return render_template('most-rated-shows.html')


@app.route('/show/<int:id>')
def show_detail(id):
    show_details = queries.get_show(id)
    seasons = queries.get_seasons_by_show_id(id)
    return render_template('show-details.html', details=show_details, seasons=seasons)


@app.route('/ordered-shows')
def render_ordered_shows():
    return render_template('ordered_shows.html')


@app.route('/birthday-actors')
def display_birthday_actors():
    return render_template('birthday-actors.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    pass


def main():
    app.run(debug=True, port=5001)


if __name__ == '__main__':
    main()
