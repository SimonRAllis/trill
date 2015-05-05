"""empty message

Revision ID: 59cfda6ff6f
Revises: None
Create Date: 2015-04-30 11:25:54.562263

"""

# revision identifiers, used by Alembic.
revision = '59cfda6ff6f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_titles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('surname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('managerfirstname', sa.String(length=80), nullable=True),
    sa.Column('managersurname', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('trill_role_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('groupname', sa.String(length=80), nullable=True),
    sa.Column('job_title_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_title_id'], ['job_titles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('groupname')
    )
    op.create_table('user_jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_title_id', sa.Integer(), nullable=True),
    sa.Column('startdate', sa.Date(), nullable=True),
    sa.Column('enddate', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['job_title_id'], ['job_titles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skill_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skillgroupname', sa.String(length=80), nullable=True),
    sa.Column('trill_role_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trill_role_group_id'], ['trill_role_groups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('skillgroupname')
    )
    op.create_table('skill_titles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skilltitlename', sa.String(length=80), nullable=True),
    sa.Column('skill_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_group_id'], ['skill_groups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('skilltitlename')
    )
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skillcode', sa.String(length=80), nullable=True),
    sa.Column('skilldescription', sa.String(length=200), nullable=True),
    sa.Column('skill_title_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_title_id'], ['skill_titles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('skillcode')
    )
    op.create_table('user_skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.Column('competence', sa.String(length=20), nullable=True),
    sa.Column('age', sa.Date(), nullable=True),
    sa.Column('confidence', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_skills')
    op.drop_table('skills')
    op.drop_table('skill_titles')
    op.drop_table('skill_groups')
    op.drop_table('user_jobs')
    op.drop_table('trill_role_groups')
    op.drop_table('users')
    op.drop_table('job_titles')
    ### end Alembic commands ###