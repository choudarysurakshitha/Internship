from fastapi import APIRouter, HTTPException
from services.reportService import ReportService

router = APIRouter(prefix="/reports", tags=["Reports"])
service = ReportService()

@router.get("/")
def get_reports():
    return service.get_all_reports()

@router.get("/{report_id}")
def get_report(report_id: int):
    rep = service.get_report_by_id(report_id)
    if not rep:
        raise HTTPException(status_code=404, detail="Report not found")
    return rep

@router.post("/")
def create_report(report: dict):
    return service.add_report(report)

@router.put("/{report_id}")
def update_report(report_id: int, updated_data: dict):
    updated = service.update_report(report_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Report not found")
    return updated

@router.delete("/{report_id}")
def delete_report(report_id: int):
    deleted = service.delete_report(report_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Report not found")
    return deleted




