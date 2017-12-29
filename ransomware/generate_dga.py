import datetime
import calendar


def generate_dga():
    today_date = datetime.date.today();

    seven_kingdoms = {
        'Monday': 'kingdom_of_the_north_house_stark',
        'Tuesday': 'kingdom_of_the_mountain_and_the_vale_house_arynn',
        'Wednesday': 'kingdom_of_the_isles_and_rivers_house_hoare',
        'Thursday': 'kingdom_of_the_rock_house_lannister',
        'Friday': 'kingdom_of_the_stormlands_house_durrandon',
        'Saturday': 'kingdom_of_the_reach_house_highgarden',
        'Sunday': 'principality_of_the_dorne'

    }

    tlds = ['.northlab', '.valelab', '.isleslab', '.rocklab', '.stormlab', '.reachlab', '.dornelab'];
    chosen_tld = tlds[today_date.day % 7]
    today_day = calendar.day_name[today_date.weekday()]

    def caesar(plainText, shift):
        cipherText = ""
        for ch in plainText:
            if ch.isalpha():
                stayInAlphabet = ord(ch) + shift
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                cipherText += finalLetter

        return cipherText

    s = "".join(x for x in seven_kingdoms[today_day].split("_"))

    ds = []
    for i in range(0, 26):
        ds.append(caesar(s, i) + hex((today_date - datetime.date(2011, 4, 17)).days)[2:] + chosen_tld);
    return ds



