# Data indices

A data index stores a collection of documents in a project. This page shows how to create and delete a data index, and to list all data indices in a project. 

Since a data index "lives" inside a project, we need to specify which project we are referring to. This is accomplished by a project key `PROJ_KEY`. We can obtain the project keys for our projects by [listing them](../guide/projects.md).


## Create data index in a project

Suppose you want to create an index called `NAME`. Optionally, a description,`DESC`, for the data index can be provided. 

=== "CLI"
    <div class="termy">

    ```console
    $ deepsearch cps data-indices create -p PROJ_KEY -n NAME -d DESC
    ```

    </div>
=== "Python"

    After you have generated the api object (from [login configuration](../installation/login.md)),

    ```python
    api.data_indices.create(proj_key=PROJ_KEY, name=NAME, desc=DESC)
    ```

In addition, it is possible to specify non-default `type` of data index. For more, see [here for CLI](../cli-reference.md#create) and [here for python](../api-reference.md#deepsearch.cps.client.components.data_indices.CpsApiDataIndices.create).


| Type           | Description                          |
| -------------- | ------------------------------------ |
| `Document`     | (Default) Index containing documents uploaded as PDF and converted by the platform. |
| `DB Records`   | Index containing data matching the DB records schema. This usually orginates from curated data collections, and exposes a schema which can be leveraged in the processing pipeline. |
| `Generic`      | Generic type with the least requirements. |
| `Experiment`   | Data coming from simulation experiments. |


---
## Listing data indices in a project

=== "CLI"
    <div class="termy">

    ```console
    $ deepsearch cps data-indices list -p PROJ_KEY
    ```

    </div>
=== "Python"
    ```python
    indices = api.data_indices.list(PROJ_KEY)

    for item in indices:
        print(item.key, item.name)

    # If your project uses Pandas, you can easily convert the list of projects to a Dataframe
    import pandas as pd
    df = pd.DataFrame([item.to_dict() for item in indices])
    print(df)
    ```
---

## Deleting data index in a project

To delete a data index, you need to specify an index via its `INDEX_KEY`. [Listing data indices](#listing-data-indices-in-a-project) will show the `INDEX_KEY` for all the indices in a project.

=== "CLI"
    <div class="termy">

    ```console
    $ deepsearch cps data-indices delete -p PROJ_KEY -x INDEX_KEY
    ```

    </div>
=== "Python"
    ```python
    from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource

    # specify index
    coords = ElasticProjectDataCollectionSource(proj_key=PROJ_KEY, index_key=INDEX_KEY)

    api.data_indices.delete(coords)
    ```

---

## Adding documents in a project

Documents can be converted and added, directly, to a data index in a project. Briefly, documents can be on a local machine or on the remote files. Local documents can be in PDF format, ZIP archives, or directory containing both (`PATH_DOCS`). The web address of a remote document is input directly or multiple web addresses can be stored in a text file (`PATH_URL`). The specification of documents is same as in [Document Conversion](../guide/convert-doc.md).


=== "CLI"
    <div class="termy">

    ```console
    // for local documents
    $ deepsearch cps data-indices upload -p PROJ_KEY -x INDEX_KEY -i PATH_DOCS
    
    // for online documents
    $ deepsearch cps data-indices upload -p PROJ_KEY -x INDEX_KEY -u PATH_URL
    ```

    </div>
=== "Python"
    ```python
    from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource

    # Specify index
    coords = ElasticProjectDataCollectionSource(proj_key=PROJ_KEY, index_key=INDEX_KEY)

    # For local documents
    ds.data_indices_utilities.upload_files(coords=coords, local_file=PATH_DOCS)

    # For online documents

    # load the urls from the file to a list
    input_urls = open(PATH_URL).readlines()
    # or, define a list directly
    #input_urls = ["https:///URL1", "https://URL2", "https://URL3"]

    ds.data_indices_utilities.upload_files(coords=coords, url=input_urls)
    ```

---