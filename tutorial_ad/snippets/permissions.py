from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    code snippet의 owner만 수정할 수 있게 하는 custom permission이다.
    """

    def has_object_permission(self, request, view, obj):
        #읽기 권한은 어떤 요청에든 허용되어진다
        # 따라서 GET, HEAD, OPTIONS 요청은 항상 허용한다
        if request.method in permissions.SAFE_METHODS:
            return True
        # 쓰기 권한은 snippet의 owner만 허용하도록 한다
        return obj.owner == request.user