# Quelque astuces pour lire les dictionnaires

## Les clés

Je peux créer une liste avec uniquement les **clés** de mon dictionnaire

```python
priority_levels = {
    "h": "Haute",
    "m": "Moyenne",
    "b": "Basse",
    "t": "Top",
}

print(priority_levels.keys())
# → ['h', 'm', 'b']
```

## Les valeurs

Je peux créer une liste avec uniquement les **valeurs** de mon dictionnaire

```python
priority_levels = {
    "h": "Haute",
    "m": "Moyenne",
    "b": "Basse",
    "t": "Top",
}

print(priority_levels.values())
# → ['Haute', 'Moyenne', 'Basse']
```

## Les deux !

Je peux aussi faire de mon dictionnaire une liste avec tuple pour chaque élément de mon dictionnaire

```python
priority_levels = {
    "h": "Haute",
    "m": "Moyenne",
    "b": "Basse",
    "t": "Top",
}

print(priority_levels.items())
# → [
#       ('h', 'Haute'),
#       ('m', 'Moyenne'),
#       ('b', 'Basse'),
#       ('t', 'Top')
# ]
```