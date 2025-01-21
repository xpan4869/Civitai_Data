# Civitai_Data
## Background
Data Source: Civitai REST API <https://github.com/civitai/civitai/wiki/REST-API-Reference>

## Creators
| Name              |   Type   | Description |
| :---------------- | :------: | ----: |
| username         |   String   |The username of the creator|
| modelCount       |   number   | The amount of models linked to this user |
| link             |  string    | Url to get all models from this user |
| image            |  string     | Url to get profile image (avatar) of this user |

## Models
https://civitai.com/api/v1/models
| Name              |   Type   | Description |
| :---------------- | :------: | ----: |
| id         |   number   |The identifier for the model|
| name       |   string   | The name of the model |
| **description**     |  string    | The description of the model (HTML)|
| type            |  enum (Checkpoint, TextualInversion, Hypernetwork, AestheticGradient, LORA, Controlnet, Poses)| The model type|
| tags       |  string     | Url to get profile image of this user |
| mode       |  enum (Archived, TakenDown) / null | The mode in which the model is currently on. If Archived, files field will be empty. If TakenDown, images field will be empty |
| creator         |   string   |The name of the creator|
| upload_data             |  string    | Url to get all models from this user |
| last_version_date       |  string     | Url to get profile image of this user |
| stats_download_coun       |  number    | The number of downloads the model has |
| stats_favorite_count      |  number    | Url to get all models from this user |
| stats_comment_count       |  number     | The number of comments the model has |
| stats_rating_count       |  number     | The number of ratings the model has |
| stats_rating       |  number     | The average rating of the model |

## ModelVersions
https://civitai.com/api/v1/model-versions/:id
| Name              |   Type   | Description |
| :---------------- | :------: | ----: |
| id         |   number   |The identifier for the model|
| name       |   string   | The name of the model |
| **description**     |  string    | The description of the model (HTML)|
| type            |  enum (Checkpoint, TextualInversion, Hypernetwork, AestheticGradient, LORA, Controlnet, Poses)| The model type|
| tags       |  string     | Url to get profile image of this user |
| mode       |  enum (Archived, TakenDown) / null | The mode in which the model is currently on. If Archived, files field will be empty. If TakenDown, images field will be empty |
| creator         |   string   |The name of the creator|
| upload_data             |  string    | Url to get all models from this user |
| last_version_date       |  string     | Url to get profile image of this user |
| stats_download_coun       |  number    | The number of downloads the model has |
| stats_favorite_count      |  number    | Url to get all models from this user |
| stats_comment_count       |  number     | The number of comments the model has |
| stats_rating_count       |  number     | The number of ratings the model has |
| stats_rating       |  number     | The average rating of the model |



| download_url       |  number     | The average rating of the model |

## Images
stats
