import aiohttp
from modules.libraries.dbms import Database


class Sender:
    def __init__(self, db: str, discussion_id: int, message: str, userID: int):
        self._db = Database(db)
        self._discussion_id = discussion_id
        self._message = message
        self._userID = userID
        self._api_url = "https://forum.wayzer.ru/api/posts"

    async def format_status(self, status: int) -> str:
        return {
            200: "Сообщение успешно отправлено",
            201: "Сообщение успешно отправлено",
            401: "Ошибка! Неавторизован",
            403: "Ошибка! Доступ запрещен",
            404: "Ошибка! Обсуждение не найдено",
            500: "Ошибка! Ошибка сервера",
        }.get(status, "Ошибка! Неизвестная ошибка")

    async def send_message(self) -> str:
        try:
            info = await self._db.fetch_info("userID", self._userID)
            flarum = info.get("flarum")

            headers = {
                "Authorization": f"Token {flarum}",
                "Content-Type": "application/json",
            }

            data = {
                "data": {
                    "type": "posts",
                    "attributes": {
                        "content": self._message,
                    },
                    "relationships": {
                        "discussion": {
                            "data": {
                                "type": "discussions",
                                "id": self._discussion_id,
                            }
                        }
                    },
                }
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self._api_url, headers=headers, json=data
                ) as response:
                    return await self.format_status(response.status)

        except aiohttp.ClientError as e:
            return f"Ошибка сети: {e}"
        except Exception as e:
            return f"Произошла ошибка: {e}"
