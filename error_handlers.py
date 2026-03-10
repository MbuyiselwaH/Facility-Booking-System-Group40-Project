from flask import render_template
from app import app


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors with custom page"""
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    """Handle 403 Forbidden errors"""
    return render_template('errors/403.html'), 403

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 Internal Server errors"""
    return render_template('errors/500.html'), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all unhandled exceptions"""
    
    app.logger.error(f'Unhandled exception: {str(e)}')
    
   
    if app.debug:
        raise e
    return render_template('errors/500.html'), 500