import os



basedir = os.path.abspath(os.path.dirname(__file__))
#数据库连接代码
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#数据迁移文件保存位置
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#以下两条不一定要
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SQLALCHEMY_TRACK_MODIFICATIONS = True


