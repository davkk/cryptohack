# General - Encoding

1. ASCII - vim

Sformatowanie liczb tak aby każda była w osobnej linijce:

```
:s/, //g
```

Wykonanie komendy na całym pliku:

```
:%s/\d\+/\=nr2char(submatch(0))/g
```

Zaznaczenie wszystkich linii (`ggVG`), oraz sklejenie w jedną linijkę (`gJ`).

2. Hex

```bash
$ echo -n 63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d | xxd -r -p
```

3. Base64

```bash
$ echo -n 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf | xxd -r -p | base64
```


4. Bytes and Big Integers

```bash
$ bc <<< "obase=16;11515195063862318899931685488813747395775516287289682636499965282714637259206269" | xxd -r -p
```

5. Encoding Challenge

```bash
$ go run ./encoding-challenge.go
base64 jeffrey_ran_sealed
bigint documentary_stationery_shoes
bigint slots_visits_diamonds
hex paying_evaluations_victor
utf-8 gotta_without_gabriel
hex snap_acre_guidance
rot13 crop_aboriginal_toner
bigint faqs_catering_board
base64 fabulous_lite_priced
utf-8 likes_pd_flour
hex closes_terror_tie
bigint lodge_dreams_r
base64 vegetarian_johns_assistant
utf-8 carey_catalogs_reaches
hex vampire_hc_complexity
utf-8 loop_hugo_schedule
rot13 unions_om_watson
utf-8 drawn_specials_cj
hex canadian_states_citizen
rot13 intro_pb_funds
hex clips_idle_short
hex regulatory_ratings_shown
base64 permission_pace_unit
base64 before_irc_millions
hex dictionary_compatibility_secured
rot13 attempting_mit_fellowship
hex garage_jets_grounds
utf-8 transcription_enforcement_promote
hex lady_appliance_ist
hex governing_meat_pg
hex voice_valid_kim
utf-8 babies_affiliated_packaging
hex couples_nickel_evaluation
rot13 paso_choose_highlight
hex inflation_rice_pointed
bigint marks_albania_resulted
base64 funds_syndicate_painting
utf-8 lib_investigations_vii
base64 limitation_grace_sensitive
bigint fully_punch_scene
bigint replacing_gallery_dod
base64 croatia_anna_simpson
utf-8 titled_graham_tribute
base64 occurring_people_advantages
hex ef_therapist_lance
bigint debut_maritime_pvc
bigint les_wishes_intimate
rot13 calculate_favor_prototype
rot13 interact_closing_watt
utf-8 custody_prints_saver
hex congressional_before_blue
rot13 label_magnet_drama
base64 detective_gathered_using
bigint palace_hp_things
base64 logical_pure_cakes
rot13 riding_sad_anatomy
utf-8 speeds_proudly_disclose
base64 singapore_url_battery
bigint donated_enhanced_spot
bigint candidates_maps_nikon
bigint age_online_rabbit
rot13 para_cl_seek
utf-8 twins_silk_pharmacy
utf-8 swaziland_composer_although
rot13 hair_spectacular_monthly
bigint pharmacology_assumptions_durable
rot13 referral_horn_guides
rot13 interests_commander_detected
bigint denied_gain_cathedral
rot13 reliable_refurbished_commodities
rot13 cnet_bride_disks
rot13 jaguar_occurring_rental
bigint pace_defining_provide
rot13 belongs_shoe_qualification
hex revenge_bound_lid
utf-8 followed_packing_invasion
base64 result_mine_symbols
rot13 id_moderator_partially
rot13 angeles_relevant_harbor
utf-8 finishing_mud_cement
base64 delivery_pens_petersburg
hex introduced_creations_period
base64 spirits_claim_grant
bigint directories_mobiles_consortium
utf-8 phd_parks_parallel
bigint seat_normally_testing
base64 organisation_sigma_since
hex sensor_dosage_conservation
hex required_tomato_dying
base64 personalized_double_reducing
rot13 liz_expertise_tons
bigint produces_pharmacy_hq
hex adolescent_safari_louisiana
hex rocket_meal_pre
bigint entrepreneurs_sea_environments
rot13 angel_waterproof_zope
base64 unix_industries_typically
base64 replaced_many_nova
base64 ladder_purchased_avon
bigint creek_den_journalism
crypto{3nc0d3_d3c0d3_3nc0d3}
```
