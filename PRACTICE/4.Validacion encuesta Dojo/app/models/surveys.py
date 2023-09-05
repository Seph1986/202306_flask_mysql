from flask import flash

class Survey:

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.ubicacion = data["ubicacion"]
        self.idioma = data["idioma"]
        self.comentario = data["comentario"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    
    @staticmethod
    def validate_data(data):
        valid = True

        if len(data["user_name"]) < 3:
            valid = False
            flash("Name too short", "warning")
        if data["location"] == "-- Select a Location --":
            valid = False
            flash("Choose a location","warning")
        if data["language"] == "-- Select a Language --":
            valid = False
            flash("Choose a language","warning")
        if len(data["comment"]) < 1:
            valid = False
            flash("No text on message","warning")

        return valid