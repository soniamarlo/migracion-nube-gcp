# [START gae_python_mysql_app]
import os
import webapp2
import MySQLdb


# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get("CLOUDSQL_CONNECTION_NAME")
CLOUDSQL_USER = os.environ.get("CLOUDSQL_USER")
CLOUDSQL_PASSWORD = os.environ.get("CLOUDSQL_PASSWORD")


def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv("SERVER_SOFTWARE", "").startswith("Google App Engine/"):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join("/cloudsql", CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD,
        )

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
    else:
        db = MySQLdb.connect(
            host="34.175.97.150", user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD
        )

    return db


class MainPage(webapp2.RequestHandler):
    def get(self):
        """Simple request handler that shows all of the MySQL variables."""
        self.response.headers["Content-Type"] = "text/plain"

        db = connect_to_cloudsql()
        cursor = db.cursor()
        cursor.execute("SHOW VARIABLES")

        for r in cursor.fetchall():
            self.response.write("{}\n".format(r))


app = webapp2.WSGIApplication(
    [
        ("/", MainPage),
    ],
    debug=True,
)

# [END gae_python_mysql_app]