from flask import Blueprint, jsonify, request
from .services.game_service import GameService
from .validators.move_validator import MoveValidator

# Create blueprints for different parts of the application
game_bp = Blueprint('game', __name__)
validator = MoveValidator()
game_service = GameService()

@game_bp.route('/grid')
def get_grid():
    return jsonify(game_service.get_grid())

@game_bp.route('/validate', methods=['POST'])
def validate_move():
    data = request.json
    validation_result = validator.validate_move(data)
    if not validation_result['valid']:
        return jsonify(validation_result)
    
    return jsonify(game_service.validate_move(
        data.get('row'),
        data.get('col'),
        data.get('number')
    ))

def register_routes(app):
    app.register_blueprint(game_bp, url_prefix='/api/v1')