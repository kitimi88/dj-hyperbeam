from django.shortcuts import render,get_object_or_404, redirect
from .models import Poll, Choice, Vote
from django.views.generic import DetailView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import ChoiceForm
from django.contrib import messages


def poll_list(request):
    polls = Poll.objects.all()
    latest_polls = Poll.objects.order_by('-updated')[0:3]

    query = request.GET.get('q')
    if query:
        polls = Poll.objects.filter(Q(title__icontains=query)).distinct()

    paginator = Paginator(polls,6)
    page = request.GET.get('page')
    try:
        polls = paginator.page(page)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)

    context = {
        'polls':polls,
        'latest_polls':latest_polls
    }
    return render(request,'polls/poll_list.html',context)



def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    vote_form = ChoiceForm()
    if not poll.active:
        return render(request, 'polls/poll_result.html', {'poll': poll})
    loop_count = poll.choice_set.count()
    context = {
        'poll': poll,
        'vote_form':vote_form,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'polls/poll_detail.html', context)



def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id) 


    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        vote_form = ChoiceForm(data=request.POST)
        choice = Choice.objects.get(id=choice_id)
        
        if vote_form.is_valid():
            vote = Vote( poll=poll, choice=choice)
           # vote = vote_form.save(commit=False)
            vote.poll = poll
            vote.save()
            print(vote)
            return render(request, 'polls/poll_result.html', {'poll': poll})
    else:
        vote_form = ChoiceForm()
        messages.error(
            request, "No choice selected!", extra_tags='alert alert-warning alert-dismissible fade show')
        return redirect("polls:detail", poll_id)
    
    return render(request, 'polls/poll_result.html', {'poll': poll,'vote_form':vote_form})

# def poll_vote(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)

#     choice_id = request.POST.get('choice')


#     if choice_id:
#         choice = Choice.objects.get(id=choice_id)
#         vote = Vote( poll=poll, choice=choice)
#         vote.save()
#         print(vote)
#         messages.success(request, 'Thanks for voting!',extra_tags='alert alert-success alert-dismissible fade show')
#         return render(request, 'polls/poll_result.html', {'poll': poll})
#     else:
#         messages.error(
#             request, "No choice selected!", extra_tags='alert alert-warning alert-dismissible fade show')
#         return redirect("polls:detail", poll_id)
#     return render(request, 'polls/poll_result.html', {'poll': poll})

