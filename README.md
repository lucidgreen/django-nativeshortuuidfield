# NativeShortUUID

This Library is for providing a db model field that when save it, it decodes the shortuuid value to be UUID, and then store it as UUID
When read from DB, it will encode the UUID value to be shortuuid value

<h3>INSTALL:</h3>
```
  pipenv install native-shortuuid
```

<h3>USAGE:</h3>
```
  ..modelProps

  uuid = NativeShortUUIDField(unique=True, default=uuid.uuid4)
  ...
```

