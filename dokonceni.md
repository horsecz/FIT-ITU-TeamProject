Co jsem dodelal / zmenil (xhorky32):

0) App.vue: (all)
    - smazano pozadi, nastaveno jedno fixni stejne pozadi
1) Login.vue:
    - zmena stylu
    - pridana moznost registrace noveho uzivatele (=> pridan Register.vue)
2) Home.vue:
    - pridan Home do topbaru (navigace)
    - delete trips
    - zprovoznen Plan new trip (NewTrip.vue)
3) Settings.vue:
    - zmena stylu
    - pridam Home > Settings do topbaru (navigace v appce)
    - nyni uz kompletne funkcni (drive kulisa)
    - v pripade jakekoliv interakce (stisk CONFIRM po zmene) vypise hlasku
4) Trip.vue:
    - Home > Trip v topbaru
    - async addDest -> upraveno
    - async delDest
    - async addDay
    - async delDay
    - all trips fixed (zobrazoval jen ID=0, now all) [pozn. backend]
5) NewTrip.vue:
    - all
6) Register.vue:
    - all
7) Backend:
    - cokoli related ke zmenam vyse