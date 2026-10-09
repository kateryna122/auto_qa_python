from playwright.sync_api import expect

from providers.data.users_provider import UsersProvider


# def test_login_with_valid_credentials(github_ui_client):
#     user = UsersProvider.login_user_exists()
#
#     github_ui_client.login(
#         user["username"],
#         user["password"]
#     )
#
#     expect(
#         github_ui_client.page.get_by_role("heading", name="Device verification")
#     ).to_be_visible()


def test_login_with_invalid_credentials(github_ui_client):
    user = UsersProvider.login_user_non_exists()

    github_ui_client.login(
        user["username"],
        user["password"]
    )

    expect(
        github_ui_client.page.get_by_text(
            "Incorrect username or password."
        )
    ).to_be_visible()
