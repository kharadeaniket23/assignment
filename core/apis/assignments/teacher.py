from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.assignments import Assignment, AssignmentStateEnum

from .schema import AssignmentSchema, AssignmentGradeSchema
teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    teachers_assignments = Assignment.get_assignments_by_teacher()
    teachers_assignments = Assignment.get_assignments_by_teacher(p.teacher_id)
    filtered_assignments = [assignment for assignment in teachers_assignments if assignment.state in ['SUBMITTED', 'GRADED']]

    teachers_assignments_dump = AssignmentSchema().dump(teachers_assignments, many=True)
    return APIResponse.respond(data=teachers_assignments_dump)

def list_assignments(p):
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    
    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
def grade_assignment(p, incoming_payload):
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
