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
| description     |  string    | The description of the model (HTML)|
| type            |  enum (Checkpoint, TextualInversion, Hypernetwork, AestheticGradient, LORA, Controlnet, Poses)| The model type|
| nsfw       |  boolean     | Whether the model is NSFW or not |
| tags       |  string     | Url to get profile image of this user |
| creator         |   string   |The name of the creator|
| upload_data             |  string    | Url to get all models from this user |
| stats_download_coun       |  number    | The number of downloads the model has |
| stats_favorite_count      |  number    | Url to get all models from this user |
| stats_comment_count       |  number     | The number of comments the model has |
| stats_rating_count       |  number     | The number of ratings the model has |
| stats_rating       |  number     | The average rating of the model |

## ModelVersions
https://civitai.com/api/v1/model-versions/:id
| Name              |   Type   | Description |
| :---------------- | :------: | ----: |
| model_id         |   number   |The identifier for the model|
| version_id         |   number   |The identifier for the model version|
| version_name       |   string   | The name of the model version |
| version_description     |  string    | The description of the model version (usually a changelog)|
| created_at             |  Date    | The date in which the version was created |
| download_url       |  string    |The download url to get the model file for this specific version|
| training_words      |  string    | The words used to trigger the model|
| base_model       |  string     |       |

## Images
https://civitai.com/api/v1/images
| Name              |   Type   | Description |
| :---------------- | :------: | ----: |
| image_id         |   number   |The id of the image|
| url       |   string   |The url of the image at it's source resolution|
| hash       |   string   | The name of the model |
| model_id         |   number   |The ID of a model to get images from (model gallery)|
| post_id         |   number   |The ID of a post to get images from|
| modelVersionId  |   number   |The ID of a model version to get images from (model gallery filtered to version)|
| width     |  number    | The width of the image)|
| height    |  number | The height of the image |
| nsfw       |  boolean     | If the image has any mature content labels |
| nsfwLevel    |  enum (None, Soft, Mature, X)	     | The NSFW level of the image |
| created_at       |  date     | The date the image was posted |
| cry_count         |   number   | The number of cry reactions |
| laugh_count             |  number    | The number of laugh reactions |
| like_count       |  number    | The number of like reactions |
| heart_count       |  number    | The number of heart reactions |
| comment_cout       |  number    | The number of downloads the model has |
| meta       |  object    |The generation parameters parsed or input for the image|
