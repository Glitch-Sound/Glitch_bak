from sqlalchemy.orm import Session, aliased     # type: ignore

import sys
sys.path.append('~/app')

from model.summary_item import SummaryItem
from model.summary_user import SummaryUser
from model.user import User
from model.tree import Tree


def getSummariesItem(db: Session, rid: int):
    try:
        query = db.query(
            SummaryItem.rid_items.label('rid'),
            SummaryItem.task_risk,
            SummaryItem.task_count_idle,
            SummaryItem.task_count_run,
            SummaryItem.task_count_alert,
            SummaryItem.task_count_review,
            SummaryItem.task_count_complete,
            SummaryItem.task_count_total,
            SummaryItem.task_workload_total,
            SummaryItem.task_number_completed,
            SummaryItem.task_number_total,
            SummaryItem.bug_risk,
            SummaryItem.bug_count_idle,
            SummaryItem.bug_count_run,
            SummaryItem.bug_count_alert,
            SummaryItem.bug_count_review,
            SummaryItem.bug_count_complete,
            SummaryItem.bug_count_total,
            SummaryItem.bug_workload_total,
            SummaryItem.date_entry
        )\
        .filter(SummaryItem.rid_items == rid)\
        .order_by(SummaryItem.date_entry)

        result = query.all()
        return result

    except Exception as e:
        raise e


def getSummariesUser(db: Session, rid: int):
    try:
        UserAlias = aliased(User)

        query = db.query(
            SummaryUser.rid,
            SummaryUser.id_project,
            UserAlias.rid.label('rid_users'),
            UserAlias.name.label('name'),
            SummaryUser.task_risk,
            SummaryUser.task_count_idle,
            SummaryUser.task_count_run,
            SummaryUser.task_count_alert,
            SummaryUser.task_count_review,
            SummaryUser.task_count_complete,
            SummaryUser.task_count_total,
            SummaryUser.task_workload_total,
            SummaryUser.task_number_completed,
            SummaryUser.task_number_total,
            SummaryUser.bug_risk,
            SummaryUser.bug_count_idle,
            SummaryUser.bug_count_run,
            SummaryUser.bug_count_alert,
            SummaryUser.bug_count_review,
            SummaryUser.bug_count_complete,
            SummaryUser.bug_count_total,
            SummaryUser.bug_workload_total,
            SummaryUser.date_entry
        )\
        .join(UserAlias,  UserAlias.rid == SummaryUser.rid_users)\
        .filter(SummaryUser.rid_users == rid)\
        .order_by(SummaryUser.date_entry)

        result = query.all()
        return result

    except Exception as e:
        raise e


def getAncestorsItem(db: Session, rid: int):
    try:
        query = db.query(
            Tree.rid_ancestor.label('rid')
        )\
        .filter(Tree.rid_descendant == rid)\
        .filter(Tree.rid_descendant != Tree.rid_ancestor)\
        .order_by(Tree.rid_ancestor)

        result = query.all()
        return result

    except Exception as e:
        raise e
