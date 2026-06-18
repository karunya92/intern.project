from auth.auth_utils import hash_password, verify_password


def test_password_hash_round_trip():
    stored = hash_password("secret")
    assert verify_password("secret", stored)
    assert not verify_password("wrong", stored)
