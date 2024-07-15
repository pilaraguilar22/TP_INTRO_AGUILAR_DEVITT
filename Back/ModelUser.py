from .user import User
class ModelUser:
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql= """SELECT id, username, password, fullname FROM usser
                WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.chack_password(row[2],user.password))
            else:
                return None
        except Exception as ex:
            raise Exception(ex)#veo si la clave hashaeda coicide con la contra