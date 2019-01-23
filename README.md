# Overview

An app that allows a user to create and manage their ballroom profiles. This
also lets them select competitions and look for partners registered for that
competitions and contact them.

# Database design

## Tables

### Location
| Field | Type |
| ----- | ---- |
| zip code | Integerfield |
| city | Charfield |
| street address | Charfield |

### Competition

| Field | Type |
| ----- | ---- |
| Name | Charfield |
| Location | address |
| Registration link | url |
| Competition home page | url |

### Profile
| Field | Type |
| ---- | ----- |
| user | FK to User |
| DOB | Datetimefield |
| height | Integerfield |
| how serious | Integer |
| o2cm link | url |
| summary | Charfield |
| description | Textfield |
| profile picture | Imagefield |
| time commitment | Float |
| affiliated university | Choice of Charfield |

### DanceStyle
| Field | Type |
| ----- | ---- |
| profile | FK to profile |
| style | Charfield |
| level | Integerfield |

### ProfileVideo
| Field | Type |
| ----- | ---- |
| profile | FK to profile |
| link | url |
| video file | Videofile |
| description | Textfield|

### UserCompetition
| Field | Type |
| ----- | ---- |
| profile | FK to profile |
| competition | FK to competition |

# API Layer

## Profile

/profiles

list of all profiles

/profiles/{id}

Get a specific profile

## Videos

/videos

query_params = profile_id

list all videos for a profile

/videos/{id}

query_params = profile_id

get a specific video for a profile


## Competition

/competitions

get all competitions


## Profilecompetition

/profilecompetitions

query_params = profile_id, competitions

get the specified competitions for a profile

# Features

1. Register / Sign in

    Allows a user to register or sign in to the app.

2. Create a profile

    Allows a user to create a new profile or edit their existing profile.

3. Select competitions

    Allows a profile to select competitions they are attending.

4. See match profiles

    See other profiles that match your filters.

5. Look up a specific profile

    Look up a specific profile that you are interested in. Ability look up some info and contact them in app.
