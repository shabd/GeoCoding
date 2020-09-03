try:
    from run import app
    import unittest

except Exception as e:
    print("Some Modules are Missing {}".format(e))


class AddressToGeoTest(unittest.TestCase):
    # Check for response 200 on /geo
    def test_geo(self):
        tester = app.test_client(self)
        response = tester.get("/geo")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #     check if the content returned is json
    def test_geo_content(self):
        tester = app.test_client(self)
        response = tester.get("/geo")
        self.assertEqual(response.content_type, "application/json")


class GeoToAddress(unittest.TestCase):
    # Check for response 200 on /geo
    def address(self):
        tester = app.test_client(self)
        response = tester.get("/address")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #     check if the content returned is json
    def test_geo_content(self):
        tester = app.test_client(self)
        response = tester.get("/address")
        self.assertEqual(response.content_type, "application/json")


if __name__ == "main":
    unittest.main()
