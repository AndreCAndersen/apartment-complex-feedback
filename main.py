import fire
from acf.app import app


class FeedbackCli:

    def run_server(self):
        app.run(host='0.0.0.0', use_reloader=False, threaded=True)


if __name__ == '__main__':
    fire.Fire(FeedbackCli)
