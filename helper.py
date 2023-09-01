def most_winner(ff):
    ff['Champion'].value_counts().reset_index()
    win_wc = ff['Champion'].value_counts().reset_index()
    return win_wc


def countrywise_ana(ef):
    team_ana = ef['team'].reset_index().drop(['index'], axis=1)
    return team_ana






def yearwise_ana(ff,y):
    year_ana=ff[ff['Year'] == y]
    web_ff = year_ana.groupby('Year').sum()[
        ['Host', 'Teams', 'Champion', 'Runner-Up', 'TopScorrer', 'Attendance', 'Matches']].reset_index()
    return web_ff


def hostwise_ana(ff,y):
    year_ana = ff.groupby('Year').sum()[
        ['Host', 'Teams', 'Champion', 'Runner-Up', 'TopScorrer', 'Attendance', 'Matches']]
    web_ff=year_ana[year_ana['Host'] == y]
    return web_ff
