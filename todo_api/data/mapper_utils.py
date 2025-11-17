from shared.models.items_dtos import Item, NewItem
from todo_api.data.entities.data_item import DataItem


def update_data_item_from_model(data_item: DataItem, item: Item | NewItem) -> DataItem:
    data_item.user_ulid = item.user_ulid
    data_item.title = item.title
    data_item.description = item.description
    data_item.done = item.done

    return data_item


def data_item_to_model(data_item: DataItem):
    return Item(
        ulid=data_item.ulid,
        user_ulid=data_item.user_ulid,
        title=data_item.title,
        description=data_item.description,
        done=data_item.done,
    )
