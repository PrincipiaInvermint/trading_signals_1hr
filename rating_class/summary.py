def summary_stars(s):

    if (s['4hr'] == '3 stars' and s['1dia'] == '3 stars'):
        return '3 stars'

    if (s['4hr'] == '4 stars' and s['1dia'] == '3 stars'):
        return '3 stars'

    if (s['4hr'] == '5 stars' and s['1dia'] == '3 stars'):
        return '3 stars'

    if (s['4hr'] == '4 stars' and s['1dia'] == '4 stars'):
        return '4 stars'

    if (s['4hr'] == '3 stars' and s['1dia'] == '4 stars'):
        return '4 stars'

    if (s['4hr'] == '3 stars' and s['1dia'] == '5 stars'):
        return '4 stars'

    else:
        return '5 stars'