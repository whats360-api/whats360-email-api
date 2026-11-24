import io, json, unittest
from send_email import send_email

class FakeResp(io.BytesIO):
    def __enter__(self): return self
    def __exit__(self, *a): return False

class T(unittest.TestCase):
    def test_request_shape(self):
        seen = {}
        def opener(req):
            seen["url"] = req.full_url; seen["auth"] = req.headers["Authorization"]; seen["body"] = json.loads(req.data)
            return FakeResp(b'{"ok": true, "data": {"message": "Email sent successfully"}}')
        out = send_email("TOKEN", "a@x.test", "b@y.test", "S", "B", opener)
        self.assertEqual(seen["url"], "https://whats360.live/api/v1/email/send")
        self.assertEqual(seen["auth"], "Bearer TOKEN")
        self.assertEqual(seen["body"], {"from": "a@x.test", "to": "b@y.test", "subject": "S", "body": "B"})
        self.assertTrue(out["ok"])
if __name__ == "__main__": unittest.main()
