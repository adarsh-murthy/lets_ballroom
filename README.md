# Overview

An app that allows a user to create and manage their ballroom profiles. This
also lets them select competitions and look for partners registered for that
competitions and contact them.

# Database design

## Tables

### Profile
| Field | Type |
| ---- | ----- |
| user | FK to User |
| Age | Integer |
| Height | Integerfield |
| How serious | Integer |
| o2cm link | url |
| videos | FK to Video |
| Summary | Charfield |
| Description | Textfield |
| Profile picture | Imagefield |
| style | Choice |
| level | Integerfield |
| location | choice of cities |
| Time commitment | Float |
| Affiliated university | Choice of Charfield |

### Video
| Field | Type |
| ----- | ---- |
| link | url |
| video file | Videofile |
| description | Textfield|

### UserCompetition
| Field | Type |
| ----- | ---- |
| profile | FK to profile |
| competition | FK to competition |

### Competition

| Field | Type |
| ----- | ---- |
| Name | Charfield |
| Location | address |
| Registration link | url |
| Competition home page | url |

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
