from tictactoe.main import app
from fastapi.testclient import TestClient


empty_board = "None,None,None,None,None,None,None,None,None"
# empty_board = [[None, None, None], [None, None, None], [None, None, None]]
client = TestClient(app)


def test_get_all_games():
    res = client.get("/api/v1/games/")
    assert res.status_code == 200


def test_create_game():
    payload = {"players": [{"name": "me"}, {"name": "other"}], "starting_player": "me"}

    res = client.post("/api/v1/games/create", json=payload)

    assert res.status_code == 201
    # assert res.json()["players"][0]["name"] == "me"
    # assert res.json()["players"][0]["symbol"] == "X"
    # assert res.json()["players"][1]["name"] == "other"
    # assert res.json()["players"][1]["symbol"] == "O"
    # assert res.json()["next_player"] == "me"
    assert res.json()["starting_player"] == "me"
    assert res.json()["winner"] == None
    assert res.json()["movements"] == 0
    assert res.json()["board_status"] == empty_board


def test_create_game_with_no_starting_player():
    payload = {"players": [{"name": "me"}, {"name": "other"}]}
    res = client.post("/api/v1/games/create", json=payload)
    assert res.status_code == 201
    # assert res.json()["players"][0]["name"] == "me"
    # assert res.json()["players"][0]["symbol"] == "X"
    # assert res.json()["players"][1]["name"] == "other"
    # assert res.json()["players"][1]["symbol"] == "O"
    # when starting player is not provided, by default is the first one
    assert res.json()["next_player"] == payload["players"][0]["name"]
    assert res.json()["winner"] == None
    assert res.json()["movements"] == 0
    assert res.json()["board_status"] == empty_board
