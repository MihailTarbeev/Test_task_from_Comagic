from uc_http_requester.requester import Request



def get_authorization_request(domain: str, api_key: str, email: str) -> Request:
    return Request(
                url = f'https://{domain}/v2api/auth/login',
                method=Request.Method.post,
                json={"email": email, "api_key": api_key},
            )

def get_index_request(domain: str, branch: str, token: str, params: dict):
    return Request(
                url = f'https://{domain}/v2api/{branch}/customer/index',
                method=Request.Method.post,
                headers={"X-ALFACRM-TOKEN": token},
                json=params,
    )