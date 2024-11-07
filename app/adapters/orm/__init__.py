"""ORM."""

from sqlalchemy.orm import registry, relationship, foreign, column_property
from sqlalchemy import and_, select

from app.adapters.orm import tables
from app.domain import models


mapper_registry = registry()
metadata = tables.metadata


def bind_mappers():
    """Binds ORM mappers"""

    mapper_registry.map_imperatively(models.TicketMessage, tables.ticket_messages_table)

    # mapper_registry.map_imperatively(models.EventDay, tables.event_days_table)
    # mapper_registry.map_imperatively(models.HolidayDay, tables.holiday_days_table)
    # mapper_registry.map_imperatively(models.CalendarChange, tables.calendar_changes_table)
    # mapper_registry.map_imperatively(models.ExtraDay, tables.extra_days_table)
    #
    # mapper_registry.map_imperatively(
    #     models.Holiday,
    #     tables.holidays_table,
    #     properties={
    #         "days": relationship(
    #             models.HolidayDay,
    #             lazy="immediate",
    #             cascade="all, delete-orphan",
    #             uselist=True,
    #         ),
    #     }
    # )
    #
    # # todo сделать версионирование чтобы изменение ивента влекло за собой изменение work_periods_table.version
    # mapper_registry.map_imperatively(
    #     models.WorkPeriod,
    #     tables.work_periods_table,
    #     properties={
    #         "extra_days": relationship(
    #             models.ExtraDay,
    #             lazy="immediate",
    #             cascade="all, delete-orphan",
    #             uselist=True,
    #         ),
    #         'holidays': relationship(
    #             models.HolidayDay,
    #             primaryjoin=and_(
    #                 tables.work_periods_table.c.start_date <= foreign(tables.holiday_days_table.c.day),
    #                 tables.work_periods_table.c.end_date >= foreign(tables.holiday_days_table.c.day)
    #             ),
    #             lazy="immediate",
    #             uselist=True,
    #             viewonly=True,
    #         ),
    #         "period_events": relationship(
    #             models.CalendarEvent,
    #             primaryjoin="and_(WorkPeriod.id == CalendarEvent.work_period_id, CalendarEvent.self_expense == False)",
    #             lazy="immediate",
    #             cascade="all, delete-orphan",
    #             uselist=True,
    #         ),
    #         "period_events_self_expense": relationship(
    #             models.CalendarEvent,
    #             primaryjoin="and_(WorkPeriod.id == CalendarEvent.work_period_id, CalendarEvent.self_expense == True)",
    #             lazy="immediate",
    #             cascade="all, delete-orphan",
    #             uselist=True,
    #         ),
    #     },
    #     version_id_col=tables.work_periods_table.c.version,
    # )
    #
    # mapper_registry.map_imperatively(
    #     models.CalendarEvent,
    #     tables.calendar_events_table,
    #     properties={
    #         "event_dates": relationship(
    #             models.EventDay,
    #             lazy="immediate",
    #             cascade="all, delete-orphan",
    #             uselist=True,
    #         ),
    #         "changes": relationship(
    #             models.CalendarChange,
    #             lazy="immediate",
    #             primaryjoin=tables.calendar_events_table.c.id == tables.calendar_changes_table.c.event_id,
    #             foreign_keys=tables.calendar_events_table.c.id,
    #             remote_side=tables.calendar_changes_table.c.event_id,
    #             uselist=True,
    #             single_parent=True,
    #         ),
    #     },
    # )
    #
    # mapper_registry.map_imperatively(
    #     CalendarChangeRecord,
    #     tables.calendar_changes_table,
    #     properties={
    #         "employee_name": column_property(
    #             select(tables.employees_table.c.name)
    #             .where(tables.calendar_changes_table.c.employee_id == tables.employees_table.c.id)
    #         ),
    #         "employee_photo": column_property(
    #             select(tables.employees_table.c.photo)
    #             .where(tables.calendar_changes_table.c.employee_id == tables.employees_table.c.id)
    #         ),
    #     },
    # )
    #
    # mapper_registry.map_imperatively(
    #     CalendarEventRecord,
    #     tables.calendar_events_table,
    #     properties={
    #         "event_dates": relationship(
    #             models.EventDay,
    #             lazy="immediate",
    #             uselist=True,
    #             viewonly=True,
    #         ),
    #         "changes": relationship(
    #             models.CalendarChange,
    #             lazy="immediate",
    #             primaryjoin=tables.calendar_events_table.c.id == tables.calendar_changes_table.c.event_id,
    #             foreign_keys=tables.calendar_events_table.c.id,
    #             remote_side=tables.calendar_changes_table.c.event_id,
    #             uselist=True,
    #             single_parent=True,
    #             viewonly=True,
    #         ),
    #         "employee_name": column_property(
    #             select(tables.employees_table.c.name)
    #             .where(tables.calendar_events_table.c.employee_id == tables.employees_table.c.id)
    #         ),
    #         "employee_photo": column_property(
    #             select(tables.employees_table.c.photo)
    #             .where(tables.calendar_events_table.c.employee_id == tables.employees_table.c.id)
    #         ),
    #     },
    # )
    #
    # mapper_registry.map_imperatively(
    #     CalendarEmployeeRecord,
    #     tables.employees_table,
    #     properties={
    #         "calendar_events": relationship(
    #             models.CalendarEvent,
    #             lazy="immediate",
    #             uselist=True,
    #             viewonly=True,
    #         ),
    #     }
    # )
