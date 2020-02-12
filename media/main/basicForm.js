class Form {
    constructor(modelId, modelNamePlural, modelNameSingular, csrf_token, pType) {
        this.modelId = modelId;
        this.csrf_token = csrf_token;
        this.modelNamePlural = modelNamePlural;
        this.modelNameSingular = modelNameSingular;

        if (!pType || pType === "index") {
            this.createDeleteModal();
        }

        let _this = this;

        $(".btn-delete").on('click', function () {
            _this.confirmDelete($(this).attr("data-id"));
        });
    }

    createDeleteModal() {
        let _this = this;

        let textConfirm = $("<p>").html(`¿Está seguro que quiere eliminar el registro de ${this.modelNameSingular}?`);
        let btnClose = $("<button>").addClass("btn btn-default").attr({ "type": "button", "data-dismiss": "modal" }).html("Cancelar");
        let btnSave = $("<button>").addClass("btn btn-danger").attr({ "type": "button" }).html("Eliminar").on('click', function () {
            _this.delete();
        });

        let modalBody = $("<div>").addClass("modal-body").append(textConfirm);
        let modalFooter = $("<div>").addClass("modal-footer").append([btnClose, btnSave]);
        let modalTitle = $("<div>").addClass("modal-title");
        let spanCloseText = $("<span>").attr({ "aria-hidden": "true" }).html("&times;");
        let modalBtnTClose = $("<button>").attr({ "type": "button", "data-dismiss": "modal", "aria-label": "Cerrar" }).addClass("close").append(spanCloseText);
        let modalHeader = $("<div>").addClass("modal-header").append([modalTitle, modalBtnTClose]);
        let modalContent = $("<div>").addClass("modal-content").append([modalHeader, modalBody, modalFooter]);
        let modalDialog = $("<div>").addClass("modal-dialog modal-sm").append(modalContent);
        let divModal = $("<div>").addClass("modal fade").attr("id", "deleteModal").append(modalDialog);
        $("body").append(divModal);
    }

    confirmDelete(modelId) {
        this.modelId = modelId;
        $("#deleteModal").modal("show");
    }

    delete() {
        let _this = this;
        $.ajax({
            url: `delete/${this.modelId}`,
            data: {
            },
            success: function (r) {
                _this.successCallback(r);
            },
            error: function(r) {
                _this.errorCallback(r);
            }
        })
    }

    successCallback(r) {
        $(document).Toasts('create', {
            class: 'bg-success', 
            title: 'Correcto',
            body: 'Se ha eliminado el registro con éxito.'
        });

        $(`#tr_${this.modelId}`).remove();
        $('#deleteModal').modal('hide');
    }

    errorCallback(r) {
        $(document).Toasts('create', {
            class: 'bg-danger', 
            title: 'Oops',
            body: 'Ocurrió un error al eliminar el registro.'
        });
    }


}