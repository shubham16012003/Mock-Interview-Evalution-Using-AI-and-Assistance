from flask import Flask
from app.utils.extensions import create_app
from app.routes.interview_routes import bp
from app.routes.resume_analysis_routes import resume_analysis_bp
from app.routes.generate_resume_routes import generate_resume_bp



app = create_app()
app.register_blueprint(bp)
app.register_blueprint(resume_analysis_bp)
app.register_blueprint(generate_resume_bp)