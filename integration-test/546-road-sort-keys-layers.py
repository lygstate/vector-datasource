# layer 5
#https://www.openstreetmap.org/way/8918870
assert_has_feature(
    16, 10483, 25340, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
     "id": 8918870, "sort_rank": 447})

# layer 4
#https://www.openstreetmap.org/way/27614705
assert_has_feature(
    16, 10484, 25340, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
     "id": 27614705, "sort_rank": 446})

# layer 3
#https://www.openstreetmap.org/way/29394019
assert_has_feature(
    16, 10479, 25341, "roads",
    {"kind": "highway", "kind_detail": "motorway_link", "is_bridge": True,
     "id": 29394019, "sort_rank": 445})

# layer 2
#https://www.openstreetmap.org/way/48037053
assert_has_feature(
    16, 10484, 25339, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
     "id": 48037053, "sort_rank": 444})

# layer 1
#https://www.openstreetmap.org/way/28412298
assert_has_feature(
    16, 10472, 25323, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
     "id": 28412298, "sort_rank": 443})

# layer -1
#https://www.openstreetmap.org/way/43685501
assert_has_feature(
    16, 10472, 25323, "roads",
    {"kind": "minor_road", "kind_detail": "service", "is_tunnel": True,
     "id": 43685501, "sort_rank": 304})

# layer -2
#https://www.openstreetmap.org/way/50691047
assert_has_feature(
    16, 10491, 25323, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_tunnel": True,
     "id": 50691047, "sort_rank": 303})
