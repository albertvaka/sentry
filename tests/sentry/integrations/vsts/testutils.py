from __future__ import absolute_import

COMPARE_COMMITS_EXAMPLE = b"""
{
  "count": 1,
  "value": [
    {
      "commitId": "6c36052c58bde5e57040ebe6bdb9f6a52c906fff",
      "author": {
        "name": "max bittker",
        "email": "max@sentry.io",
        "date": "2018-04-24T00:03:18Z"
      },
      "committer": {
        "name": "max bittker",
        "email": "max@sentry.io",
        "date": "2018-04-24T00:03:18Z"
      },
      "comment": "Updated README.md",
      "changeCounts": {"Add": 0, "Edit": 1, "Delete": 0},
      "url":
        "https://mbittker.visualstudio.com/_apis/git/repositories/b1e25999-c080-4ea1-8c61-597c4ec41f06/commits/6c36052c58bde5e57040ebe6bdb9f6a52c906fff",
      "remoteUrl":
        "https://mbittker.visualstudio.com/_git/MyFirstProject/commit/6c36052c58bde5e57040ebe6bdb9f6a52c906fff"
    }
  ]
}
"""


FILE_CHANGES_EXAMPLE = b"""
{
  "changeCounts": {"Edit": 1},
  "changes": [
    {
      "item": {
        "objectId": "b48e843656a0a12926a0bcedefe8ef3710fe2867",
        "originalObjectId": "270b590a4edf3f19aa7acc7b57379729e34fc681",
        "gitObjectType": "blob",
        "commitId": "6c36052c58bde5e57040ebe6bdb9f6a52c906fff",
        "path": "/README.md",
        "url":
          "https://mbittker.visualstudio.com/DefaultCollection/_apis/git/repositories/b1e25999-c080-4ea1-8c61-597c4ec41f06/items/README.md?versionType=Commit&version=6c36052c58bde5e57040ebe6bdb9f6a52c906fff"
      },
      "changeType": "edit"
    }
  ]
}
"""
WORK_ITEM_RESPONSE = """{
  "id": 309,
  "rev": 1,
  "fields": {
    "System.AreaPath": "Fabrikam-Fiber-Git",
    "System.TeamProject": "Fabrikam-Fiber-Git",
    "System.IterationPath": "Fabrikam-Fiber-Git",
    "System.WorkItemType": "Product Backlog Item",
    "System.State": "New",
    "System.Reason": "New backlog item",
    "System.CreatedDate": "2015-01-07T18:13:01.807Z",
    "System.CreatedBy": "Jamal Hartnett <fabrikamfiber4@hotmail.com>",
    "System.ChangedDate": "2015-01-07T18:13:01.807Z",
    "System.ChangedBy": "Jamal Hartnett <fabrikamfiber4@hotmail.com>",
    "System.Title": "Hello",
    "Microsoft.VSTS.Scheduling.Effort": 8,
    "WEF_6CB513B6E70E43499D9FC94E5BBFB784_Kanban.Column": "New",
    "System.Description": "Fix this."
  },
  "_links": {
    "self": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/309"
    },
    "workItemUpdates": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/309/updates"
    },
    "workItemRevisions": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/309/revisions"
    },
    "workItemHistory": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/309/history"
    },
    "html": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/web/wi.aspx?pcguid=d81542e4-cdfa-4333-b082-1ae2d6c3ad16&id=309"
    },
    "workItemType": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c/_apis/wit/workItemTypes/Product%20Backlog%20Item"
    },
    "fields": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/fields"
    }
  },
  "url": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/309"
}"""
CREATE_SUBSCRIPTION = """
{
  "id": "fd672255-8b6b-4769-9260-beea83d752ce",
  "url": "https://fabrikam.visualstudio.com/_apis/hooks/subscriptions/fd672255-8b6b-4769-9260-beea83d752ce",
  "publisherId": "tfs",
  "eventType": "workitem.update",
  "resourceVersion": "1.0-preview.1",
  "eventDescription": "WorkItem Updated",
  "consumerId": "webHooks",
  "consumerActionId": "httpRequest",
  "actionDescription": "To host myservice",
  "createdBy": {
    "id": "00ca946b-2fe9-4f2a-ae2f-40d5c48001bc"
  },
  "createdDate": "2014-10-27T15:37:24.873Z",
  "modifiedBy": {
    "id": "00ca946b-2fe9-4f2a-ae2f-40d5c48001bc"
  },
  "modifiedDate": "2014-10-27T15:37:26.23Z",
  "publisherInputs": {
    "buildStatus": "Failed",
    "definitionName": "MyWebSite CI",
    "hostId": "d81542e4-cdfa-4333-b082-1ae2d6c3ad16",
    "projectId": "6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
    "tfsSubscriptionId": "3e8b33e7-426d-4c92-9bf9-58e163dd7dd5"
  },
  "consumerInputs": {
    "url": "https://myservice/newreceiver"
  }
}
"""
WORK_ITEM_UPDATED = """
{
  "id": "27646e0e-b520-4d2b-9411-bba7524947cd",
  "eventType": "workitem.updated",
  "publisherId": "tfs",
  "scope": "all",
  "message": {
    "text": "Bug #5 (Some great new idea!) updated by Jamal Hartnett.\r\n(http://fabrikam-fiber-inc.visualstudio.com/web/wi.aspx?pcguid=74e918bf-3376-436d-bd20-8e8c1287f465&id=5)",
    "html": "<a href=\"http://fabrikam-fiber-inc.visualstudio.com/web/wi.aspx?pcguid=74e918bf-3376-436d-bd20-8e8c1287f465&amp;id=5\">Bug #5</a> (Some great new idea!) updated by Jamal Hartnett.",
    "markdown": "[Bug #5](http://fabrikam-fiber-inc.visualstudio.com/web/wi.aspx?pcguid=74e918bf-3376-436d-bd20-8e8c1287f465&id=5) (Some great new idea!) updated by Jamal Hartnett."
  },
  "detailedMessage": {
    "text": "Bug #5 (Some great new idea!) updated by Jamal Hartnett.\r\n(http://fabrikam-fiber-inc.visualstudio.com/web/wi.aspx?pcguid=74e918bf-3376-436d-bd20-8e8c1287f465&id=5)\r\n\r\n- New State: Approved\r\n",
    "html": "<a href=\"http://fabrikam-fiber-inc.visualstudio.com/web/wi.aspx?pcguid=74e918bf-3376-436d-bd20-8e8c1287f465&amp;id=5\">Bug #5</a> (Some great new idea!) updated by Jamal Hartnett.<ul>\r\n<li>New State: Approved</li></ul>",
    "markdown": "[Bug #5](http://fabrikam-fiber-inc.visualstudio.com/web/wi.aspx?pcguid=74e918bf-3376-436d-bd20-8e8c1287f465&id=5) (Some great new idea!) updated by Jamal Hartnett.\r\n\r\n* New State: Approved\r\n"
  },
  "resource": {
    "id": 2,
    "workItemId": 0,
    "rev": 2,
    "revisedBy": null,
    "revisedDate": "0001-01-01T00:00:00",
    "fields": {
      "System.Rev": {
        "oldValue": "1",
        "newValue": "2"
      },
      "System.AuthorizedDate": {
        "oldValue": "2014-07-15T16:48:44.663Z",
        "newValue": "2014-07-15T17:42:44.663Z"
      },
      "System.RevisedDate": {
        "oldValue": "2014-07-15T17:42:44.663Z",
        "newValue": "9999-01-01T00:00:00Z"
      },
      "System.State": {
        "oldValue": "New",
        "newValue": "Approved"
      },
      "System.Reason": {
        "oldValue": "New defect reported",
        "newValue": "Approved by the Product Owner"
      },
      "System.AssignedTo": {
        "newValue": "Jamal Hartnet"
      },
      "System.ChangedDate": {
        "oldValue": "2014-07-15T16:48:44.663Z",
        "newValue": "2014-07-15T17:42:44.663Z"
      },
      "System.Watermark": {
        "oldValue": "2",
        "newValue": "5"
      },
      "Microsoft.VSTS.Common.Severity": {
        "oldValue": "3 - Medium",
        "newValue": "2 - High"
      }
    },
    "_links": {
      "self": {
        "href": "http://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/5/updates/2"
      },
      "parent": {
        "href": "http://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/5"
      },
      "workItemUpdates": {
        "href": "http://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/5/updates"
      }
    },
    "url": "http://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/5/updates/2",
    "revision": {
      "id": 5,
      "rev": 2,
      "fields": {
        "System.AreaPath": "FabrikamCloud",
        "System.TeamProject": "FabrikamCloud",
        "System.IterationPath": "FabrikamCloud\\Release 1\\Sprint 1",
        "System.WorkItemType": "Bug",
        "System.State": "New",
        "System.Reason": "New defect reported",
        "System.CreatedDate": "2014-07-15T16:48:44.663Z",
        "System.CreatedBy": "Jamal Hartnett",
        "System.ChangedDate": "2014-07-15T16:48:44.663Z",
        "System.ChangedBy": "Jamal Hartnett",
        "System.Title": "Some great new idea!",
        "Microsoft.VSTS.Common.Severity": "3 - Medium",
        "WEF_EB329F44FE5F4A94ACB1DA153FDF38BA_Kanban.Column": "New"
      },
      "url": "http://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/5/revisions/2"
    }
  },
  "resourceVersion": "1.0",
  "resourceContainers": {
    "collection": {
      "id": "c12d0eb8-e382-443b-9f9c-c52cba5014c2"
    },
    "account": {
      "id": "f844ec47-a9db-4511-8281-8b63f4eaf94e"
    },
    "project": {
      "id": "be9b3917-87e6-42a4-a549-2bc06a7a878f"
    }
  },
  "createdDate": "2016-09-19T13:03:30.6438544Z"
}
"""
