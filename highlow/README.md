# API
`/new`
- request without additional data
- response is
```json 
    { "result" : "success", 
        "data" : { 
            "card" : "<suit><value>",
            "score" : 0
        }
    }
    // OR
    { "result" : "failure",
        "data" : {
            "reason" : "<reason string>" 
        }
    }
```

`/score`
- request without additional data
- response is
```json 
    { "result" : "success", 
        "data" : { 
            "card"  : "<suit><rank>",
            "score" : "<value>"}
    }
    // OR
    { "result" : "failure",
        "data" : {
            "reason" : "<reason string>"
        }
    }
```

`/call` 
- request with your guess 
```json
    { "data" : {
        "guess" : "[high|low]" 
        }
    }
```
Upon success, player's score is incremented. The response will reflect the updated score.

- response is
```json 
    { "result" : "correct", 
        "data" : { 
            "card"  : "<suit><rank>",
            "score" : "<value>"}
    }
    { "result" : "incorrect", 
        "data" : { 
            "card"  : "<suit><rank>",
            "score" : "<value>"}
    }
    // OR
    { "result" : "failure",
        "data" : {
            "reason" : "<reason string>"
        }
    }
```
After an incorrect verdict, the game is over.
A /new round has to be requested.