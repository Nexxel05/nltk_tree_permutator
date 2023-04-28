from django.utils.datastructures import MultiValueDictKeyError
from nltk import Tree
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.tree_permutator import build_paraphrases


@api_view(["GET"])
def paraphrases_view(request):
    try:
        limit = int(request.query_params["limit"])
        if limit < 0:
            limit = 20
    except ValueError:
        return Response("'limit' query parameter must be integer")
    except MultiValueDictKeyError:
        limit = 20

    try:
        tree = Tree.fromstring(request.query_params["tree"])

        res = build_paraphrases(tree, "NP", limit)
        return Response(res)

    except MultiValueDictKeyError:
        return Response("Specify correct query parameter 'tree'")
    except ValueError:
        return Response("'tree' query parameter might be incorrect")
