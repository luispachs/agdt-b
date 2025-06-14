from sqlalchemy import select
from src.database.models.Plan import Plan
from src.Repository.PlanRepository import PlanRepository
from flask import jsonify
import json
def getPlanes():
    planRepository = PlanRepository()
    stmt = select(Plan)
    result =  planRepository.conn.execute(stmt)
    data = [tuple(x) for x in result.fetchall()]
    return {'data':data},200
