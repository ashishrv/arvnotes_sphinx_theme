import os


def setup(app):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme(
        'arvnotes_sphinx_theme', current_dir)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
}

def get_html_theme_path():
    return os.path.abspath(os.path.dirname(__file__))
